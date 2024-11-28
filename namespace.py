def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()
test_function()
# inner_function() # вызов приведет к ошибке т.к. функция является вложенной. Она доступна только внутри области видимости функции test_function