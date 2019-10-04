set term post eps color enhanced
set output 'MAESTRO_scaling2.eps'

set size 0.65, 0.65

set xlabel "# Cores [total threads]";
set ylabel "Wallclock Time [s]";

set xrange[900:250000]
set yrange[0:2]

set logs x

set grid

plot 'MAESTROeX_SCALING' u 1:4 w lp lw 3 ti "MAESTROeX Cell-Centered Projection", \
     'MAESTROeX_SCALING' u 1:5 w lp lw 3 ti "MAESTROeX Nodal Projection"
