export DASHBOARD_PATH=~/public-svn/matsim/scenarios/countries/de/berlin/projects/sounding-board/ccc/

default:
	Rscript --default-packages=tidyr --verbose CCC_dashboard_table_20230125.R
	Rscript --default-packages=tidyr --verbose CCC_dashboard_gueterverkehr.R
	head -11 CCC_dashboard_gueterverkehr.csv
	-rm ${DASHBOARD_PATH}/CCC_dashboard*.csv
	cp CCC_dashboard*.csv ${DASHBOARD_PATH}
	cd ${DASHBOARD_PATH} ; /usr/local/bin/svn update ;/usr/local/bin/svn commit -m "commit new version"

