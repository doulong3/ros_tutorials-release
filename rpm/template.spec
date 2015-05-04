Name:           ros-indigo-turtlesim
Version:        0.5.3
Release:        0%{?dist}
Summary:        ROS turtlesim package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/turtlesim
Source0:        %{name}-%{version}.tar.gz

Requires:       qt
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-rosconsole
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-roscpp-serialization
Requires:       ros-indigo-roslib
Requires:       ros-indigo-rostime
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-std-srvs
BuildRequires:  qt-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-rosconsole
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-roscpp-serialization
BuildRequires:  ros-indigo-roslib
BuildRequires:  ros-indigo-rostime
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-std-srvs

%description
turtlesim is a tool made for teaching ROS and ROS packages.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon May 04 2015 Dirk Thomas <dthomas@osrfoundation.org> - 0.5.3-0
- Autogenerated by Bloom

* Tue Dec 23 2014 Dirk Thomas <dthomas@osrfoundation.org> - 0.5.2-0
- Autogenerated by Bloom

