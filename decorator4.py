def a_decorator_passing_arguments(function_to_decorate):
     def a_wrapper_accepting_arguments(arg1, arg2):
         print("Смотри, что я получил:", arg1, arg2)
         function_to_decorate(arg1, arg2)
     return a_wrapper_accepting_arguments
@a_decorator_passing_arguments
def f(name,sirname):
    print('my name is',name,sirname)
f(input(),input())