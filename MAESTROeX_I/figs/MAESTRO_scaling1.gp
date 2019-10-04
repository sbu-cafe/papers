set term post eps color enhanced
set output 'MAESTRO_scaling1.eps'

set size 0.65, 0.65

set xlabel "# Cores [total threads]";
set ylabel "Wallclock Time [s]";

set xrange[900:250000]
set yrange[0:20]

set logs x

set grid

plot 'MAESTRO_SCALING' u 1:2 w lp lw 3 ti "MAESTRO", \
     'MAESTROeX_SCALING' u 1:2 w lp lw 3 ti "MAESTROeX", \
     'MAESTROeX_SCALING' u 1:3 w lp lw 3 ti "MAESTROeX; No Base State Evolution"
