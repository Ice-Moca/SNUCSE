int global_initialized = 7;
int global_zero_initialized = 0;
int global_not_initialized;
static int global_static_initialized = 77;
static int global_static_not_initialized;
extern int extern_variable;

#pragma weak weak_global_initialized
int weak_global_initialized = 5;

#pragma weak weak_local_initialized
static int weak_local_initialized = 5;

#pragma weak weak_function
int weak_function(int a, int b) { return a + b; }

int regular_function(int a, int b) { return a + b; }

int extern_function(int a, int b);
