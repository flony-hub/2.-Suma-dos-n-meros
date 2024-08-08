# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 20:58:46 2024

@author: auten
"""
class Solution:
    def addTwoNumbers(self, l1: list, l2: list) -> list:
        n = len(l1)
        rdo = []
        carry = 0
        for i in range(n-1, -1, -1):
            suma = l1[i] + l2[i] + carry
            unidad = suma % 10
            carry = suma // 10
            rdo.insert(0, unidad)
        if carry > 0:
            rdo.insert(0, carry)
        return rdo

l1 = [2,4,3]
l2 = [5,6,4]
objeto = Solution()
print(objeto.addTwoNumbers(l1, l2))

