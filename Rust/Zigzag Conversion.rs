struct Solutions;

impl Solutions {
    pub fn convert(s: String, num_rows: i32) -> String {
        //если количество строк равно 1, то просто возвращаем исходную 
        if num_rows == 1 {
            return s;
        }

        let mut res: String = String::new(); //задание пустой изменяемой строки, т.е. результата
        let max_offset: usize = ((num_rows * 2) - 2) as usize;//создание числа пропускаемых букв
        println!("max_offset: {}", max_offset);

        for row_index in 0..num_rows as usize {//цикл для каждой строки
            for item_index in (row_index..s.len()).step_by(max_offset) {
                res.push(s.chars().nth(item_index).expect("user error"));

                if row_index != 0 && row_index != (num_rows - 1) as usize {//проверка номера строки
                    let diagonal_offset: usize = max_offset - 2 * row_index;
                    let diagonal_item_index: usize = diagonal_offset + item_index;

                    if diagonal_item_index < s.len() {//проверка, не вышли ли индексы за пределы слова
                        res.push(s.chars().nth(diagonal_item_index).expect("user error"));
                    }
                }
            }
        }
        return res;
    }
}

fn main() {
    let resultat = Solutions::convert("PAYPALISHIRING".to_string(), 3);//to_string() для явного преобразования значения в строковой тип
    println!("{}", resultat);
}