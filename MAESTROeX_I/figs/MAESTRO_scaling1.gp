set term post eps color enhanced
set output 'MAESTRO_scaling1.eps'

set xlabel "# Cores [total threads]";
set ylabel "Wallclock Time [s]";

set xrange[900:250000]
set yrange[0:20]

set logs x

set grid

plot 'MAESTRO_SCALING' u 1:2 w lp ti "MAESTRO", \
     'MAESTROeX_SCALING' u 1:2 w lp ti "MAESTROeX", \
     'MAESTROeX_SCALING' u 1:3 w lp ti "MAESTROeX; No Base State Evolution"
