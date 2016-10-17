#!/usr/bin/env python

import sys
import struct
import time
from firebase import firebase

FIREBASE_URL = "https://meshxxxx.firebaseio.com/"

# Main
if __name__ == '__main__':

    fb = firebase.FirebaseApplication(FIREBASE_URL, None) # Create a reference to the Firebase Application


    root_cid ="5ccf7fc12xxx"
    

    tbl = "mesh_master"
    local_ip = "192.168.0.25" 
    ex_local_ip = "114.32.123.xxx"
    root_ip = "192.168.0.101"
     # updtime = time.strptime(time.time(), "%Y-%m-%d %H:%M:%S")
    updtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    newstr= [tbl, root_cid] 
    

    fb.put(tbl,root_cid, {"local_ip":local_ip, "ex_local_ip":ex_local_ip, "root_ip": root_ip, "updtime" :updtime})

     # mesh node loop start 
    

    tbl2 = "mesh_node"
    child_cid1 = "5ccf7fc18xxx"
    child_cid2 = "5ccf7fc12xxx" 
    newstr = [tbl2, root_cid,child_cid1] 
    fb.put(tbl2,root_cid, {child_cid1:1, child_cid2:2})
