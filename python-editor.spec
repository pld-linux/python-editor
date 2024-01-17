# NOTE: there is different "editor" project for python 3.4+
#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Programmatically open an editor, capture the result
Summary(pl.UTF-8):	Programowe otwieranie edytora i przechwycenie wyniku
Name:		python-editor
Version:	1.0.4
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/python-editor/
Source0:	https://files.pythonhosted.org/packages/source/p/python-editor/python-editor-%{version}.tar.gz
# Source0-md5:	0e52648a4a6e7c89e3be44e9456530b4
URL:		https://pypi.org/project/python-editor/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
python-editor is a library that provides the "editor" module for
programmatically interfacing with your system's $EDITOR.

%description -l pl.UTF-8
python-editor to biblioteka dostarczająca moduł "editor" do
programowej współpracy z systemowym $EDITOR.

%package -n python3-editor
Summary:	Programmatically open an editor, capture the result
Summary(pl.UTF-8):	Programowe otwieranie edytora i przechwycenie wyniku
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-editor
python-editor is a library that provides the "editor" module for
programmatically interfacing with your system's $EDITOR.

%description -n python3-editor -l pl.UTF-8
python-editor to biblioteka dostarczająca moduł "editor" do
programowej współpracy z systemowym $EDITOR.

%prep
%setup -q -n python-editor-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.md
%{py_sitescriptdir}/editor.py[co]
%{py_sitescriptdir}/python_editor-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-editor
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/editor.py
%{py3_sitescriptdir}/__pycache__/editor.cpython-*.py[co]
%{py3_sitescriptdir}/python_editor-%{version}-py*.egg-info
%endif
