#!/bin/bash

ruby <<EOF
Dir['?.png'].each { |f| spawn("mv #{f} 0#{f}") }
Dir['??.png'].each { |f| spawn("mv #{f} 0#{f}") }
EOF

exec convert -delay 2 -size 1000x1000 xc:White +antialias -dispose previous -loop 0 *.png animation.gif
