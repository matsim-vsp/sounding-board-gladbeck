export DASHBOARD_PATH=~/public-svn/matsim/scenarios/countries/de/berlin/projects/sounding-board/ccc/
export CURRENT_PATH=~/public-svn/matsim/scenarios/countries/de/berlin/projects/sounding-board/current/

default:
	Rscript --default-packages=tidyr --verbose CCC_dashboard_privaterPersonenverkehr_MK.R
	Rscript --default-packages=tidyr --verbose CCC_dashboard_gueterverkehr.R
	head -11 CCC_dashboard_gueter.csv
	-rm ${DASHBOARD_PATH}/CCC_dashboard*.csv
	mv CCC_dashboard*.csv ${DASHBOARD_PATH}
	cd ${DASHBOARD_PATH} ; /usr/local/bin/svn update ;/usr/local/bin/svn commit -m "commit new version"

current:
	Rscript --default-packages=tidyr --verbose CCC_dashboard_privaterPersonenverkehr_KN.R
	-rm ${CURRENT_PATH}/CCC_dashboard*.csv
	mv CCC_dashboard*.csv ${CURRENT_PATH}
	cd ${CURRENT_PATH} ; /usr/local/bin/svn update ;/usr/local/bin/svn commit -m "commit new version"
