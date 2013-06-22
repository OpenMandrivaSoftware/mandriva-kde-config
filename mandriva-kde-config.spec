%define epoch_kdelibs 30000000
%define source_date 20080919

Name: mandriva-kde-config
Summary: Mandriva KDE configuration
Version: 2009.0
Release: %mkrel 9
URL: http://www.mandriva.com
Group: Graphical desktop/KDE
BuildRoot: %_tmppath/%name-buildroot
BuildRequires: kde3-macros
Source0: %{name}-%{version}.%{source_date}.tar.bz2
# OpenOffice.org icons. Should be in a separate package
# in the future, since they're shared between kde, OOo
# and maybe others
Source1: ooo-icons.tar.bz2
Source2: opendocument-mime.tar.bz2
License: GPL
BuildArch: noarch

%description
This package regroups all specific Mandriva config file for KDE.
(kicker config etc.)

#--------------------------------------------------------------------

%package common
Group: Graphical desktop/KDE
Summary: Common configs used for Mandriva theme
Requires(pre): update-alternatives
Requires: urw-fonts

%description common
common configs used for Mandriva theme

%post common
update-alternatives --install /etc/kderc kde-config %_localstatedir/lib/mandriva/kde-profiles/common/upstream-kde-config 9

%postun common
if ! [ -e /var/lib/mandriva/kde-profiles/common/upstream-kde-config ]; then
  update-alternatives --remove kde-config /var/lib/mandriva/kde-profiles/common/upstream-kde-config
fi

%files common
%defattr(0644,root,root,755)
%dir %_localstatedir/lib/mandriva/
%dir %_localstatedir/lib/mandriva/kde-profiles/common
%_localstatedir/lib/mandriva/kde-profiles/common/*

#--------------------------------------------------------------------

%package -n powerpack-kde-config
Summary: Mandriva KDE configuration 
Group: Graphical desktop/KDE
Provides: kde-config-file = %version-%release
Requires: mandriva-theme
Requires: desktop-common-data
Requires(pre): mandriva-kde-config-common = %version-%release
Conflicts: kdelibs-common < %epoch_kdelibs:3.5.1
Conflicts: kdebase-common < 1:3.5.2-10.1.20060mdk
Obsoletes: mandriva-kde-config-file < 2008.0
Obsoletes: powerpackplus-kde-config < 2008.0 
Provides: powerpackplus-kde-config = %version-%release
Requires(preun): mandriva-kde-config-common

%pre -n powerpack-kde-config
if [ "$1" = "2" ]; then
	[ ! -h %_sysconfdir/kderc ] && rm -f %_sysconfdir/kderc ]
fi
if [ -d %_localstatedir/lib/mandriva/kde-profiles/powerpack/share/apps/kdesktop/Desktop ]; then
  rm -rf %_localstatedir/lib/mandriva/kde-profiles/powerpack/share/apps/kdesktop/Desktop
fi

%post -n powerpack-kde-config
update-alternatives --install /etc/kderc kde-config %_localstatedir/lib/mandriva/kde-profiles/powerpack/kderc 10

%postun -n powerpack-kde-config
if ! [ -e /var/lib/mandriva/kde-profiles/powerpack/kderc ]; then
  update-alternatives --remove kde-config /var/lib/mandriva/kde-profiles/powerpack/kderc
fi

%description -n powerpack-kde-config
This package regroups all specific Mandriva config file for KDE.

%files -n powerpack-kde-config
%defattr(0644,root,root,755)
%dir %_localstatedir/lib/mandriva/kde-profiles/powerpack
%_localstatedir/lib/mandriva/kde-profiles/powerpack/*

#--------------------------------------------------------------------

%package -n one-kde-config
Summary: Mandriva KDE configuration 
Group: Graphical desktop/KDE
Provides: kde-config-file = %version-%release
Requires: mandriva-theme
Requires: desktop-common-data
Requires(pre): mandriva-kde-config-common = %version-%release
Conflicts: kdelibs-common < %epoch_kdelibs:3.5.1
Conflicts: kdebase-common < 1:3.5.2-10.1.20060mdk
Obsoletes: mandriva-kde-config-file < 2008.0
Requires(preun): mandriva-kde-config-common

%description -n one-kde-config
This package regroups all specific Mandriva config file for KDE.

%pre -n one-kde-config
if [ "$1" = "2" ]; then
	[ ! -h %_sysconfdir/kderc ] && rm -f %_sysconfdir/kderc ]
fi
if [ -d %_localstatedir/lib/mandriva/kde-profiles/one/share/apps/kdesktop/Desktop ]; then
  rm -rf %_localstatedir/lib/mandriva/kde-profiles/one/share/apps/kdesktop/Desktop
fi

%post -n one-kde-config
update-alternatives --install /etc/kderc kde-config %_localstatedir/lib/mandriva/kde-profiles/one/kderc 10

%postun -n one-kde-config
if ! [ -e /var/lib/mandriva/kde-profiles/one/kderc ]; then
  update-alternatives --remove kde-config /var/lib/mandriva/kde-profiles/one/kderc
fi

%files -n one-kde-config
%defattr(0644,root,root,755)
%dir %_localstatedir/lib/mandriva/kde-profiles/one
%_localstatedir/lib/mandriva/kde-profiles/one/*


#--------------------------------------------------------------------

%package -n flash-kde-config
Summary: Mandriva KDE configuration 
Group: Graphical desktop/KDE
Provides: kde-config-file = %version-%release
Requires: mandriva-theme
Requires: desktop-common-data
Requires(pre): mandriva-kde-config-common = %version-%release
Conflicts: kdelibs-common < %epoch_kdelibs:3.5.1
Conflicts: kdebase-common < 1:3.5.2-10.1.20060mdk
Obsoletes: mandriva-kde-config-file < 2008.0
Requires(preun): mandriva-kde-config-common

%description -n flash-kde-config
This package regroups all specific Mandriva config file for KDE.

%pre -n flash-kde-config
if [ "$1" = "2" ]; then
	[ ! -h %_sysconfdir/kderc ] && rm -f %_sysconfdir/kderc ]
fi
if [ -d %_localstatedir/lib/mandriva/kde-profiles/flash/share/apps/kdesktop/Desktop ]; then
  rm -rf %_localstatedir/lib/mandriva/kde-profiles/flash/share/apps/kdesktop/Desktop
fi

%post -n flash-kde-config
update-alternatives --install /etc/kderc kde-config %_localstatedir/lib/mandriva/kde-profiles/flash/kderc 10

%postun -n flash-kde-config
if ! [ -e /var/lib/mandriva/kde-profiles/flash/kderc ]; then
  update-alternatives --remove kde-config /var/lib/mandriva/kde-profiles/flash/kderc
fi

%files -n flash-kde-config
%defattr(0644,root,root,755)
%dir %_localstatedir/lib/mandriva/kde-profiles/flash
%_localstatedir/lib/mandriva/kde-profiles/flash/*


#--------------------------------------------------------------------

%package -n free-kde-config
Summary: Mandriva KDE configuration 
Group: Graphical desktop/KDE
Provides: kde-config-file = %version-%release
Requires: mandriva-theme
Requires: qt4-style-iaora
Requires: desktop-common-data
Requires(pre): mandriva-kde-config-common = %version-%release
Conflicts: kdelibs-common < %epoch_kdelibs:3.5.1
Conflicts: kdebase-common < 1:3.5.2-10.1.20060mdk
Obsoletes: mandriva-kde-config-file < 2008.0
Requires(preun): mandriva-kde-config-common
Obsoletes: download-kde-config-2007 < 2008.0 
Provides:	download-kde-config-2007
Obsoletes: discovery-kde-config < 2008.0
Provides: discovery-kde-config = %version-%release

%description -n free-kde-config
This package regroups all specific Mandriva config file for KDE.

%pre -n free-kde-config
if [ "$1" = "2" ]; then
	[ ! -h %_sysconfdir/kderc ] && rm -f %_sysconfdir/kderc ]
fi
if [ -d %_localstatedir/lib/mandriva/kde-profiles/free/share/apps/kdesktop/Desktop ]; then
  rm -rf %_localstatedir/lib/mandriva/kde-profiles/free/share/apps/kdesktop/Desktop
fi

%post -n free-kde-config
update-alternatives --install /etc/kderc kde-config %_localstatedir/lib/mandriva/kde-profiles/free/kderc 10

%postun -n free-kde-config
if ! [ -e /var/lib/mandriva/kde-profiles/free/kderc ]; then
  update-alternatives --remove kde-config /var/lib/mandriva/kde-profiles/free/kderc
fi

%files -n free-kde-config
%defattr(0644,root,root,755)
%dir %_localstatedir/lib/mandriva/kde-profiles/free
%_localstatedir/lib/mandriva/kde-profiles/free/*


#--------------------------------------------------------------------
# KDM

%package -n mandriva-kdm-config
Summary: Mandriva KDM config file
Group: Graphical desktop/KDE
Obsoletes: kdebase-kdm-config-file < 2008.0
Provides: kdm-config-file = %version-%release
# For upgrade 
Provides: kdebase-kdm-config-file = 2:%version 
Conflicts: kdebase-progs <= 3.5.1-15.1.20060mdk
Obsoletes: mandriva-kde-config-file < 2008.0
Requires(post): perl-MDK-Common

%description -n mandriva-kdm-config
Mandriva KDM config file

%trigger -n mandriva-kdm-config -- kdebase-kdm-config-file 
perl -MMDK::Common -e 'update_gnomekderc("%{_kde3_configdir}/kdm/kdmrc", "General", "ConsoleTTYs", "tty1,tty2,tty3,tty4,tty5,tty6", "ServerVTs", "-7")'

%files -n mandriva-kdm-config
%defattr(0644,root,root,0755)
%config(noreplace) %_kde3_configdir/kdm/backgroundrc
%config(noreplace) %_kde3_configdir/kdm/kdmrc
%_kde3_configdir/kdm/themes

#---------------------------------------

%prep
%setup -q -a 1 -a 2

%install
rm -rf %buildroot
# Create profile dirs
mkdir -p %buildroot/%{_kde3_configdir}
mkdir -p %buildroot/%_localstatedir/lib/mandriva

mv kde-profiles %buildroot/%_localstatedir/lib/mandriva
mv kdm %buildroot/%{_kde3_configdir}

# openoffice icons, see #26311
mkdir -p %buildroot/%_localstatedir/lib/mandriva/kde-profiles/common/share/icons/
cp -a ooo-icons/hicolor %buildroot/%_localstatedir/lib/mandriva/kde-profiles/common/share/icons/

# openoffice mimetypes, see #26311
mkdir -p %buildroot/%_localstatedir/lib/mandriva/kde-profiles/common/share/mimelnk/application
cp -a opendocument-mime/* %buildroot/%_localstatedir/lib/mandriva/kde-profiles/common/share/mimelnk/application
# XXX we have to rename them to the same name provided by kdelibs-common, otherwise the
# global ones are used.
pushd %buildroot/%_localstatedir/lib/mandriva/kde-profiles/common/share/mimelnk/application
    mv openoffice.org2.4-oasis-drawing.desktop vnd.oasis.opendocument.graphics.desktop
    mv openoffice.org2.4-oasis-drawing-template.desktop vnd.oasis.opendocument.graphics-template.desktop
    mv openoffice.org2.4-oasis-master-document.desktop vnd.oasis.opendocument.text-master.desktop
    mv openoffice.org2.4-oasis-formula.desktop vnd.oasis.opendocument.formula.desktop
    mv openoffice.org2.4-oasis-spreadsheet.desktop vnd.oasis.opendocument.spreadsheet.desktop
    mv openoffice.org2.4-oasis-spreadsheet-template.desktop vnd.oasis.opendocument.spreadsheet-template.desktop
    mv openoffice.org2.4-oasis-text.desktop vnd.oasis.opendocument.text.desktop
    mv openoffice.org2.4-oasis-text-template.desktop vnd.oasis.opendocument.text-template.desktop
    mv openoffice.org2.4-oasis-web-template.desktop vnd.oasis.opendocument.text-web.desktop
    mv openoffice.org2.4-oasis-presentation.desktop vnd.oasis.opendocument.presentation.desktop
    mv openoffice.org2.4-oasis-presentation-template.desktop vnd.oasis.opendocument.presentation-template.desktop
    mv openoffice.org2.4-spreadsheet.desktop vnd.sun.xml.calc.desktop
    mv openoffice.org2.4-spreadsheet-template.desktop vnd.sun.xml.calc.template.desktop
    mv openoffice.org2.4-presentation.desktop vnd.sun.xml.impress.desktop
    mv openoffice.org2.4-presentation-template.desktop vnd.sun.xml.impress.template.desktop
    mv openoffice.org2.4-drawing.desktop  vnd.sun.xml.draw.desktop
    mv openoffice.org2.4-drawing-template.desktop vnd.sun.xml.draw.template.desktop
    mv openoffice.org2.4-text.desktop vnd.sun.xml.writer.desktop
    mv openoffice.org2.4-text-template.desktop vnd.sun.xml.writer.template.desktop
    mv openoffice.org2.4-master-document.desktop vnd.sun.xml.writer.master.desktop
    mv openoffice.org2.4-formula.desktop vnd.sun.xml.math.desktop
popd


for name in flash free one powerpack; do
    echo "[Directories-default]" > %buildroot%_localstatedir/lib/mandriva/kde-profiles/$name/kderc
    echo "prefixes=/var/lib/mandriva/kde-profiles/common,%_localstatedir/lib/mandriva/kde-profiles/$name" >> %buildroot%_localstatedir/lib/mandriva/kde-profiles/$name/kderc
	# create the symlink to the desktop data
    mkdir -p %buildroot%_localstatedir/lib/mandriva/kde-profiles/$name/share/apps/kdesktop
    ln -s %_datadir/mdk/desktop/$name %buildroot%_localstatedir/lib/mandriva/kde-profiles/$name/share/apps/kdesktop/DesktopLinks
done

# Upstream
echo "[Directories-default]" > %buildroot%_localstatedir/lib/mandriva/kde-profiles/common/upstream-kde-config
echo "prefixes=%{_kde3_prefix}" >> %buildroot%_localstatedir/lib/mandriva/kde-profiles/common/upstream-kde-config

# Bookmarks
mkdir -p %buildroot%_localstatedir/lib/mandriva/kde-profiles/{free,flash,one,powerpack}/share/apps/konqueror/
ln -s %_datadir/mdk/bookmarks/konqueror/bookmarks-download.xml %buildroot%_localstatedir/lib/mandriva/kde-profiles/free/share/apps/konqueror/bookmarks.xml
ln -s %_datadir/mdk/bookmarks/konqueror/bookmarks-one.xml %buildroot%_localstatedir/lib/mandriva/kde-profiles/one/share/apps/konqueror/bookmarks.xml
ln -s %_datadir/mdk/bookmarks/konqueror/bookmarks-one.xml %buildroot%_localstatedir/lib/mandriva/kde-profiles/flash/share/apps/konqueror/bookmarks.xml
ln -s %_datadir/mdk/bookmarks/konqueror/bookmarks-powerpack.xml %buildroot%_localstatedir/lib/mandriva/kde-profiles/powerpack/share/apps/konqueror/bookmarks.xml

%clean
rm -rf %buildroot
