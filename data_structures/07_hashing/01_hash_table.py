#!/usr/bin/env python3
from number_theory.prime_numbers import next_prime


class HashTable:
    """
        Basic Hash Table example with open addressing and linear probing
    """

    def __init__(self, size_table, charge_factor=None, lim_charge=None):
        self.size_table = size_table
        self.values = [None] * self.size_table
        self.lim_charge = 0.75 if lim_charge is None else lim_charge
        self.charge_factor = 1 if charge_factor is None else charge_factor
        self.__aux_list = []
        self._keys = {}

    def keys(self):
        return self._keys

    def balanced_factor(self):
        return sum([1 for slot in self.values
                    if slot is not None]) / (self.size_table * self.charge_factor)

    def hash_function(self, key):
        return key % self.size_table

    def _step_by_step(self, step_ord):

        print("step {0}".format(step_ord))
        print([i for i in range(len(self.values))])
        print(self.values)

    def bulk_insert(self, values):
        i = 1
        self.__aux_list = values
        for value in values:
            self.insert_data(value)
            self._step_by_step(i)
            i += 1

    def _set_value(self, key, data):
        self.values[key] = data
        self._keys[key] = data

    def _colision_resolution(self, key, data=None):
        # key: 0, data: 10
        new_key = self.hash_function(key + 1)
        print('new_key: %s' % new_key)  # 1

        while self.values[new_key] is not None \
                and self.values[new_key] != key:

            if self.values.count(None) > 0:
                new_key = self.hash_function(new_key + 1)
            else:
                new_key = None
                break

        return new_key

    def rehashing(self):
        survivor_values = [value for value in self.values if value is not None]
        self.size_table = next_prime(self.size_table, factor=2)
        self._keys.clear()
        self.values = [None] * self.size_table #hell's pointers D: don't DRY ;/
        map(self.insert_data, survivor_values)

    def insert_data(self, data):
        print('data: %s' % data)  # 10
        key = self.hash_function(data)
        print('key: %s' % key)  # 0

        print('values: %s \n_keys: %s' % (self.values, self._keys))
        # values: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        # _keys: {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}

        if self.values[key] is None:
            self._set_value(key, data)

        elif self.values[key] == data:
            pass

        else:
            colision_resolution = self._colision_resolution(key, data)
            print('colision_resolution: %s' % colision_resolution)  # None
            if colision_resolution is not None:
                self._set_value(colision_resolution, data)
            else:
                self.rehashing()
                self.insert_data(data)
        print('values: %s \n_keys: %s' % (self.values, self._keys))
        print()

    def __str__(self):
        return 'size_table: %s \nvalues: %s\nlim_charge: %s \ncharge_factor: %s \
               \n__aux_list: %s \n_keys: %s' % (self.size_table, self.values, \
               self.lim_charge, self.charge_factor, self.__aux_list, self._keys)


if __name__ == '__main__':
    hash_table = HashTable(10)
    print(hash_table)
    print()
    for i in range(5):
        hash_table.insert_data(i)
    print()
    hash_table.insert_data(10)
    print()
    print(hash_table)



