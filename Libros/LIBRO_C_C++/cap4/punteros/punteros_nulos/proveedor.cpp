#include <iostream>

int main(){
    int * proveedor = nullptr; /*en C++ se hace asi ya que NULL no tiene tipo y arrastraba algunos errores, se mejoro en C++*/
    std::cout<<proveedor;
    return 0;
}