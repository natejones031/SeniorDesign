#include <boost/python.hpp>
using namespace boost::python

BOOST_PYTHON_MODULE(pixy_functions)
{
// def("cpp function name", cpp function name);

/* creates connection with pixy and listens for mssgs
* returns: 0 for successful connections
* others returns error mssg
*/
def("pixy_init",pixy_init); 
// indicates when new blocks data is received
def("pixy_blocks_are_new",pixy_blocks_are_new);
// returns block data
def("pixy_get_blocks",pixy_get_blocks);
// terminates connection with pixy
def("pixy_close",pixy_close);
// sends description of error to stdout
def("pixy_error",pixy_error);
}