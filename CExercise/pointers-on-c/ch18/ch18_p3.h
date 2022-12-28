typedef char* va_list;
#define va_start(varArg, lastFixedArg) varArg = (char *)(&lastFixedArg) + sizeof(lastFixedArg)
#define va_arg(varArg, type) *((type *)varArg)++
#define va_end(varArg)