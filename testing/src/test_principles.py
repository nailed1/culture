import sys
# TODO make with 'pip install -e .'
sys.path.append('./src')

from math_demo import add
from math_demo import add_with_bug

#Раннее тестирование позволяет сэкономить время и ресурсы, выявляя ошибки на ранних этапах разработки. Это помогает избежать накопления ошибок и упрощает их исправление, что в конечном итоге приводит к более качественному продукту.
#Тесты показывают наличие ошибок, а не их отсутствие. Даже если все тесты проходят успешно, это не гарантирует, что в коде нет ошибок. Тесты могут быть неполными или не охватывать все возможные сценарии использования, поэтому важно продолжать тестирование и улучшать его со временем.
#Тесты должны покрывать кластеры входных данных. Это означает, что тесты должны быть разработаны таким образом, чтобы охватывать различные категории входных данных, включая граничные случаи и типичные сценарии использования. Это помогает выявить ошибки, которые могут возникать при работе с различными типами данных и обеспечивает более надежное тестирование.

def test_addition_basic():
    assert add(1, 2) == 3
    print("Test addition passed")

def test_bug_addition_notsufficient():
    assert add_with_bug(1, 2) == 3
    assert add_with_bug(2, 3) == 5
    print("Test addition with bug passed")

def test_bug_addition_enough():
    assert add_with_bug(1, 2) == 2
    assert add_with_bug(2, 3) == 6
    print("Test addition with bug passed")

def test_addition_duplicated_logic():
    #
    assert add(6, 3) == 9
    assert add(7, 3) == 10

def test_addition_overcomplicated():
    for i in range(10, 2**32):
        for j in range(10, 2**32):
            assert add(i, j) == i + j #bad since violates duplication
            assert add(-i, j) == -i+j
            assert add(i, -j) == i-j
            assert add(-i, -j) == -i-j

if __name__ == "__main__":
    test_addition_basic()
    test_bug_addition_notsufficient()
    test_bug_addition_enough()
    test_addition_duplicated_logic()
    test_addition_overcomplicated()