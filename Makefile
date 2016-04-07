RELEASE=$(shell git describe --tags)

shinyalarm-${VERSION}.spec : shinyalarm.spec
	sed -e "s#VERSION#${VERSION}#" -e "s#RELEASE#${RELEASE}#" -e "w${@}" ${<}

shinyalarm-${VERSION} :
	mkdir ${@}
	git -C ${@} init
	git -C ${@} remote add origin git@github.com:desertedscorpion/helplessmountain.git
	git -C ${@} fetch origin

shinyalarm-${VERSION}.tar : shinyalarm-${VERSION}
	git -C ${<} archive --prefix shinyalarm-${VERSION}/ tags/${VERSION} > ${@}

shinyalarm-${VERSION}.tar.gz : shinyalarm-${VERSION}.tar
	gzip --to-stdout ${<} > ${@}

buildsrpm/shinyalarm-${VERSION}-${RELEASE}.src.rpm : shinyalarm-${VERSION}.spec shinyalarm-${VERSION}.tar.gz
	mkdir --parents buildsrpm
	mock --buildsrpm --spec shinyalarm-${VERSION}.spec --sources shinyalarm-${VERSION}.tar.gz --resultdir buildsrpm

rebuild/shinyalarm-${VERSION}-${RELEASE}.x86_64.rpm : buildsrpm/shinyalarm-${VERSION}-${RELEASE}.src.rpm
	mkdir --parents rebuild
	mock --rebuild buildsrpm/shinyalarm-${VERSION}-${RELEASE}.src.rpm --resultdir rebuild
