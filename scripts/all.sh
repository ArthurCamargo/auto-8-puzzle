#!/bin/bash
./avalia_astar_h1.sh $1 #> avalia_astar_h1.test
./avalia_astar_h2.sh $1 #> avalia_astar_h2.test
./avalia_bfs.sh      $1 #> avalia_bfs.test
./avalia_dfs.sh      $1 #> avalia_dfs.test
