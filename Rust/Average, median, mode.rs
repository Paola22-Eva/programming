use std::collections::HashMap;

fn calculation_of_values(numbers: Vec<i32>) -> (f64, f64, i32) {
    //расчет среднего значения
    let summa: i32 = numbers.iter().sum(); // Сумма всех элементов
    let mean = summa as f64 / numbers.len() as f64; // Вычисление среднего значения

    //расчет медианы
    let mut sorted_numbers = numbers.clone(); //копирование вектора
    sorted_numbers.sort(); //сортировка копии вектора чисел
    let len = sorted_numbers.len(); //длина вектора
    
    let median: f64; //переменная для медианы

    if len % 2 == 1 {
        //если количество элементов нечетное, то берем центральное
        median = sorted_numbers[len / 2] as f64;
    } else {
        //иначе медиана является средним из двух центральных элементов
        let the_first_number = sorted_numbers[len / 2 - 1];
        let the_second_number = sorted_numbers[len / 2];
        median = (the_first_number + the_second_number) as f64 / 2.0;
    }

    //расчет моды
    let mut occurrences = HashMap::new();
    for &num in &numbers {
        //подсчет кол-ва одинаковых чисел
        *occurrences.entry(num).or_insert(0) += 1; // * - дает доступ к значениям для возможности их изменить entry - поиск записи с ключом num или вставка нового ключа num; or_insert(0) - вставляет 0, если значения нет, или возвращает ссылку на значение, если значение есть
    }
    //поиск числа (моды)
    let mut max_count = 0;
    let mut mode = 0;
    
    for (&num, &count) in &occurrences {
        if count > max_count {
            max_count = count;
            mode = num;
        }
    }
    //результат:
    return (mean, median, mode)
}

fn main() {
    let numbers = vec![1, 1, 1, 1, 3, 4, 4, 6, 4];
    let (mean, median, mode) = calculation_of_values(numbers);

    println!("Среднее значение: {}", mean);
    println!("Медиана: {}", median);
    println!("Мода: {}", mode);
}
