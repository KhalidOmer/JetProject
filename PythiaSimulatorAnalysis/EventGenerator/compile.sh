export PYTHIAPATH=/usr/local

echo
echo "Compiling with : "
echo "$ROOTSYS    : "${ROOTSYS}
echo "$PYTHIAPATH : "${PYTHIAPATH}
echo

g++ Generate.cc $PYTHIAPATH/lib/libpythia8.a -o Generate -I$ROOTSYS/include  -I$PYTHIAPATH/include  -L $ROOTSYS/lib `$ROOTSYS/bin/root-config --glibs` -std=c++11
