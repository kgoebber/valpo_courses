<html>


<script language="Javascript" type="text/javascript">
<!-- Begin
function show_tab(nam)
   {
   document.getElementById("one").style.display= "none";
   document.getElementById("two").style.display= "none";
   document.getElementById("three").style.display= "none";
   document.getElementById("four").style.display= "none";
   document.getElementById("five").style.display= "none";
   document.getElementById("six").style.display= "none";
   document.getElementById("seven").style.display= "none";
   document.getElementById("eight").style.display= "none";
   document.getElementById("nine").style.display= "none";
   document.getElementById("ten").style.display= "none";
   document.getElementById("eleven").style.display= "none";
   document.getElementById("twelve").style.display= "none";
   document.getElementById("thirteen").style.display= "none";
   document.getElementById("fourteen").style.display= "none";
   document.getElementById("fifteen").style.display= "none";
   document.getElementById("sixteen").style.display= "none";
   document.getElementById("seventeen").style.display= "none";
   document.getElementById("eighteen").style.display= "none";
   document.getElementById("nineteen").style.display= "none";
   document.getElementById(nam).style.display = "block";
   }
</script>


<?php

$date = $_GET['date'];
$date2 = strftime("%y%m%d", strtotime($date));
$prevday = strftime("%Y%m%d", strtotime($date)-86400);
$nextday = strftime("%Y%m%d", strtotime($date)+86400);
$currdaystring = strftime("%d %B %Y", strtotime($date));
$nextdaystring = strftime("%d %B %Y", strtotime($date)+86400);

print "<h2 style=\"margin: 3px;\"><a href=\"probgrids.php?date=$prevday\"><<</a> | ";
print "<a href=\"probgrids.php?date=$nextday\">>></a>Model vs Observed Reports 12Z $currdaystring - 12Z $nextdaystring<br/></h2>";
?>
<a href="distros.php">Distributions</a> | <a href="scores.php">Scores</a> | Neighborhood v. Practically Perfect Forecasts | <a href="june3.php">June 3rd Case Study</a><br/>
<table border="0" cellspacing="1" cellpadding="3"><tr bgcolor="#CFCFCF">
<th>Thresholds</th><th>UH (m2s-2)</th><th>Updraft (ms-1)</th><th>Downdraft (ms-1)</th><th>Reflectivity (dBz)</th><th>10mWind (ms-1)</th><th>Notes</th></tr><tr bgcolor="#EFEFEF">
<td>"A"</td><td>75</td><td>30</td><td>-6</td><td>58</td><td>25</td><td>first guess</td></tr><tr bgcolor="#EFEFEF">
<td>"B"</td><td>54</td><td>23.35</td><td>-6.54</td><td>54.875</td><td>24.45</td><td>chosen so .005% of points hit (44876 points) for each field during experiment</tr></table>

<?php
if (!file_exists("./research/probgrid_neighbor_all_$date.grb.png")) {
	print "<h2>Probability grid not available</h2><br/>\n";
} else {
	print "Fcst using A: <a href=\"\" OnMouseOver=\"show_tab('one')\">Neighborhood</a> | PracPerfect -- Hits using A: ";
	print "<a href=\"\" OnMouseOver=\"show_tab('two')\">All</a> | ";
	print "<a href=\"\" OnMouseOver=\"show_tab('three')\">Refl</a> | ";
	print "<a href=\"\" OnMouseOver=\"show_tab('four')\">UH</a> | ";
	print "<a href=\"\" OnMouseOver=\"show_tab('five')\">10mWind</a> | ";
	print "<a href=\"\" OnMouseOver=\"show_tab('six')\">Updraft</a> | ";
	print "<a href=\"\" OnMouseOver=\"show_tab('seven')\">Downdraft</a><br/>";
	print "Fcst using B: <a href=\"\" OnMouseOver=\"show_tab('eight')\">Neighborhood</a> | ";
	print "<a href=\"\" OnMouseOver=\"show_tab('twelve')\">PracPerfect</a> -- Hits using B: ";
	print "<a href=\"\" OnMouseOver=\"show_tab('fourteen')\">All</a> | ";
	print "<a href=\"\" OnMouseOver=\"show_tab('fifteen')\">Refl</a> | ";
	print "<a href=\"\" OnMouseOver=\"show_tab('sixteen')\">UH</a> | ";
	print "<a href=\"\" OnMouseOver=\"show_tab('seventeen')\">10mWind</a> | ";
	print "<a href=\"\" OnMouseOver=\"show_tab('eighteen')\">Updraft</a> | ";
	print "<a href=\"\" OnMouseOver=\"show_tab('nineteen')\">Downdraft</a><br/>";
	print "Obs: <a href=\"\" OnMouseOver=\"show_tab('nine')\">Obs</a> | ";
	print "<a href=\"\" OnMouseOver=\"show_tab('ten')\">Neighborhood</a> | ";
	print "<a href=\"\" OnMouseOver=\"show_tab('eleven')\">NeighborhoodScaled</a> | ";
	print "<a href=\"\" OnMouseOver=\"show_tab('thirteen')\">PracPerfect</a><br/>";
	
	print "<div id=\"one\" style=\"display:block;\"><img src=\"./research/probgrid_neighbor_all_$date.grb.png\"></div>";
	print "<div id=\"two\" style=\"display:none;\"><img src=\"./research/all/binarygrid_all_$date.grb.png\"></div>";
	print "<div id=\"three\" style=\"display:none;\"><img src=\"./research/binarygrid_1kmrefl58_$date.grb.png\"></div>";
	print "<div id=\"four\" style=\"display:none;\"><img src=\"./research/binarygrid_UH75_$date.grb.png\"></div>";
	print "<div id=\"five\" style=\"display:none;\"><img src=\"./research/binarygrid_10mwind25_$date.grb.png\"></div>";
	print "<div id=\"six\" style=\"display:none;\"><img src=\"./research/binarygrid_updraft30_$date.grb.png\"></div>";
	print "<div id=\"seven\" style=\"display:none;\"><img src=\"./research/binarygrid_downdraft6_$date.grb.png\"></div>";
	print "<div id=\"eight\" style=\"display:none;\"><img src=\"./research/all5e-5/probgrid_neighbor_all_$date.grb.png\"></div>";
	print "<div id=\"nine\" style=\"display:none;\"><img src=\"./research/binarygrid_obs_$date.grb.png\"></div>";
	print "<div id=\"ten\" style=\"display:none;\"><img src=\"./research/probgrid_obs_$date.grb.png\"></div>";
	print "<div id=\"eleven\" style=\"display:none;\"><img src=\"./research/probgrid_obsscaled_$date.grb.png\"></div>";
	print "<div id=\"twelve\" style=\"display:none;\"><img src=\"./research/probgrid_pp_$date.grb.png\"></div>";
	print "<div id=\"thirteen\" style=\"display:none;\"><img src=\"./research/probgrid_obspp_$date.grb.png\"></div>";
	print "<div id=\"fourteen\" style=\"display:none;\"><img src=\"./research/binarygrid_all_$date.grb.png\"></div>";
	print "<div id=\"fifteen\" style=\"display:none;\"><img src=\"./research/binarygrid_RF_$date.grb.png\"></div>";
	print "<div id=\"sixteen\" style=\"display:none;\"><img src=\"./research/binarygrid_uh_$date.grb.png\"></div>";
	print "<div id=\"seventeen\" style=\"display:none;\"><img src=\"./research/binarygrid_UU_$date.grb.png\"></div>";
	print "<div id=\"eighteen\" style=\"display:none;\"><img src=\"./research/binarygrid_UP_$date.grb.png\"></div>";
	print "<div id=\"nineteen\" style=\"display:none;\"><img src=\"./research/binarygrid_DN_$date.grb.png\"></div>";
}
print "<img src=\"http://www.spc.noaa.gov/climo/reports/{$date2}_rpts.gif\">\n";
print "<img src=\"http://www.spc.noaa.gov/products/outlook/archive/2008/day1otlk_{$date}_1200_prt.gif\">\n";

?>

</html>
