#include <boost/python.hpp>
#include <string>

// c++ function to expose to python
const std::string greet()
{
   return std::string("hello, world");
}
 
BOOST_PYTHON_MODULE(hello_ext)
{
    using namespace boost::python;
    def("greet", greet);
}
