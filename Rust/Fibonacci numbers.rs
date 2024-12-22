use std::io;//импорт модуля для возможности чтения введенных данных std - стандартная библиотека

fn main() {
    println!("Ввод количества чисел Фибоначчи");
    //создание изменяемой строки для ввода
    let mut input = String::new();
    //чтение ввода
    io::stdin()//stdin()- функция доступа к вводу
        .read_line(&mut input)//чтение строки из stdin
        .expect("Не удалось прочитать строку");//обработка ошибки

    //преобразование  введённой строки в дробное число 
    let n: u32 = input.parse().expect("Введите число!");//тип данных целое число без знака
    let mut the_first_number = 0;//первое число Фибоначчи
    let mut the_second_number = 1;//второе число Фибоначчи

    println!("Последовательность чисел Фибоначчи");
    for i in 0..n {
        println!("{}", the_first_number);//вывод текущего числа
        let next_number = the_first_number + the_second_number;//расчет следующего числа 
        the_first_number = the_second_number; //обновление значений
        the_second_number = next_number;
    }
}