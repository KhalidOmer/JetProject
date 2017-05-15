export FJINSTALL=/usr/local

echo
echo "Compiling with : "
echo "$ROOTSYS    : "${ROOTSYS}
echo "$FJINSTALL : "${FJINSTALL}
echo

g++ -o Analyze Analyze.cc -I$ROOTSYS/include -I$FJINSTALL/include  -L $ROOTSYS/lib `$ROOTSYS/bin/root-config --glibs` `$FJINSTALL/bin/fastjet-config --cxxflags --libs --plugins` -lNsubjettiness -lEnergyCorrelator   -std=c++11
