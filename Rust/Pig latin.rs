fn pig_latin(input: &str) -> String {
    let letters = "aAeEiIoOuU"; // Строка с гласными буквами
    let mut result = String::new(); //строка с итоговым результатом

    for word in input.split_whitespace() { //деление строки на слова (функция делит строку по пробелам)
        let mut symbol = word.chars(); //chars() - перебор символов

        // Просто извлекаем первый символ без проверки
        let first_char = symbol.clone().next().unwrap(); //извлекаем первый символ

        if letters.contains(first_char) { //первый символ входит в список гласных
            result.push_str(word);
            result.push_str("-hay"); //добавление в конец слова "-hay"
        } else { // Если первый символ согласная
            let mut pig_word = String::new();
            pig_word.push_str(&word[1..]);
            pig_word.push('-');
            pig_word.push(first_char); 
            pig_word.push_str("ay "); 
            result.push_str(&pig_word); 
        }
    }

    return result
}

fn main() {
    let input = "first apple orange bed";
    let result = pig_latin(input);
    println!("{}", result);
}