#include <stdio.h>

void print_ledger(int arg) {
    #ifdef OPTION_LONG
        print_ledger_long(arg);
    #endif
    #ifdef OPTION_DETAILED
        print_ledger_detailed(arg);
    #endif
    #if !defined(OPTION_LONG) and !defined(OPTION_DETAILED)
            print_ledger_default(arg);
    #endif
}