from haversine import haversine as haversine

from geo_neighbours import neighbours_list
from geo_neighbours.geo_hash_calculation import geoHash


class GeoNeighbours:
    prefix_points_mapper = {}

    def __init__(self, points_list):
        """
        list: [{
            "latitude": "",
            "longitude": "",
            "full_address": ""
        }]
        """
        self.fillList(points_list)

    def fillList(self, points_list):
        hash_list = points_list
        for hashes in hash_list:
            geohash = geoHash(hashes.get("latitude"), hashes.get("longitude"))
            want = geohash[:5]
            if want not in self.prefix_points_mapper:
                self.prefix_points_mapper[want] = []
                self.prefix_points_mapper[want].append(
                    [hashes.get("latitude"), hashes.get("longitude"), hashes.get("full_address")])
            else:
                self.prefix_points_mapper[want].append(
                    [hashes.get("latitude"), hashes.get("longitude"), hashes.get("full_address")])

    def getNearbyStores(self, latitude, longitude):
        geohash = geoHash(latitude, longitude)
        neighbour = [
            ['b', 'c', 'f', 'g', 'u', 'v', 'y', 'z'],
            ['8', '9', 'd', 'e', 's', 't', 'w', 'x'],
            ['2', '3', '6', '7', 'k', 'm', 'q', 'r'],
            ['0', '1', '4', '5', 'h', 'j', 'n', 'p']
        ]
        neighbour_transpose = [
            ['p', 'r', 'x', 'z'],
            ['n', 'q', 'w', 'y'],
            ['j', 'm', 't', 'v'],
            ['h', 'k', 's', 'u'],
            ['5', '7', 'e', 'g'],
            ['4', '6', 'd', 'f'],
            ['1', '3', '9', 'c'],
            ['0', '2', '8', 'b']
        ]
        position = {}
        for row in range(0, 8):
            for col in range(0, 4):
                position[neighbour_transpose[row][col]] = [row, col]
        cell = 0
        want = geohash[4]
        geohash = geohash[:4]
        nearest_stores = []

        for row in range(0, 4):
            for col in range(0, 8):
                if neighbour[row][col] == want:
                    cell = row * 8 + col
        count_stores = 0
        neighbours_list[cell].insert(0, [want, [0, 0]])
        for geo_hash_by_changing_2nd_last_char in range(len(neighbours_list[cell])):
            changed_geo_hash = geohash
            row = position[changed_geo_hash[3]][0]
            col = position[changed_geo_hash[3]][1]
            row = row + neighbours_list[cell][geo_hash_by_changing_2nd_last_char][1][0]
            col = col + neighbours_list[cell][geo_hash_by_changing_2nd_last_char][1][1]
            if 0 <= row <= 7 and 0 <= col <= 3:
                changed_geo_hash = changed_geo_hash[:-1]
                changed_geo_hash = changed_geo_hash + neighbour_transpose[row][col]
            else:
                continue
            flag = 0
            changed_geo_hash = changed_geo_hash + neighbours_list[cell][geo_hash_by_changing_2nd_last_char][0]
            if changed_geo_hash in self.prefix_points_mapper:
                for geo_hash_by_changing_last_char in range(0, len(self.prefix_points_mapper[changed_geo_hash])):
                    nearest_stores.append([str(self.prefix_points_mapper[changed_geo_hash]
                                                    [geo_hash_by_changing_last_char][2]),
                                           float(self.prefix_points_mapper[changed_geo_hash][
                                                     geo_hash_by_changing_last_char][0]),
                                           float(self.prefix_points_mapper[changed_geo_hash]
                                                 [geo_hash_by_changing_last_char][1])])
                    count_stores = count_stores + 1
                    if count_stores > 20:
                        flag = 1
                        break
            if flag == 1:
                break
        nearest_stores.sort()
        nearest_stores = nearest_stores[:10]
        return nearest_stores
