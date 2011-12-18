order="
 set xr [0:100];
 set terminal png;
 set output \"result.png\";
 plot \"./result.txt\" w l;
"

echo $order | gnuplot
gpicview result.png