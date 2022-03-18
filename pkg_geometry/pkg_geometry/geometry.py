#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 15:31:19 2022

@author: molierenguile-makao
"""


class facequadri:
    def __init__(self, larg, long, haut=None):
        """

        Parameters
        ----------
        larg : TYPE float
            DESCRIPTION. the weight
        long : TYPE float
            DESCRIPTION. the lenght
        haut : TYPE, optional float
            DESCRIPTION. the height The default is None.

        Returns
        -------
        facequadri object
        
        Use
        ---
        >>> from pkg_geometry import geometry as gt
        >>> fig_geom=gt.facequadri(3,4,2)

        """
        self.lrg = larg
        self.log = long
        self.hat = haut

    # Method to computer the perimete 
    def perimetre(self):
        if self.hat is None:
            return 2 * (self.log + self.lrg)
        else:
            return 2 * (self.log + self.lrg + self.hat)

    # the method to compute the volume 
    def volume(self):
        if self.hat is None:
            return self.lrg * self.log
        else:
            return self.lrg * self.log * self.hat
    # the method that computes the area
    def surface(self):
        if self.hat is None:
            return self.log * self.lrg
        else:
            return 2 * (self.log * self.lrg + self.hat * self.lrg + self.hat * self.log)
