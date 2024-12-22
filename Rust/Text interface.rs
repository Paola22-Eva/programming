use std::collections::HashMap;
use std::io::{self, Write};

fn main() {
    let mut departments: HashMap<String, Vec<String>> = HashMap::new();

    loop {//бесконечный цикл
        //меню
        println!("Меню:");
        println!("1) добавить сотрудника в отдел");
        println!("2) показать сотрудников отдела");
        println!("3) показать всех сотрудников компании");
        println!("4) выйти");
        print!("Выберите опции от 1 до 4");
        io::stdout().flush().unwrap();// flush() заставляет сразу выводить на экран

        let mut choice = String::new();
        io::stdin().read_line(&mut choice).unwrap();//ожидание ввода пользователя, stdin - поток ввода для получения данных с пользователя
        let choice: i32 = choice.trim().parse().unwrap(); //считывание выбора и превращение в число

        match choice {
            1 => {
                println!("Введите имя сотрудника:");
                let mut name = String::new();
                io::stdin().read_line(&mut name).unwrap();
                let name = name.trim(); 

                println!("Введите название отдела:");
                let mut department = String::new();
                io::stdin().read_line(&mut department).unwrap();
                let department = department.trim();

                //добавление сотрудника в отдел
                let entry = departments.entry(department.to_string()).or_insert(Vec::new());//entry позволяет получить доступ к записи в хэш-карте
                entry.push(name.to_string()); //добавление имени сотрудника
                println!("{} добавлен в отдел {}.", name, department);
            }
            2 => {
                //список сотрудников конкретного отдела
                println!("Введите название отдела:");
                let mut department = String::new();
                io::stdin().read_line(&mut department).unwrap();
                let department = department.trim(); 
                
                if let Some(employees) = departments.get(department) {
                    println!("Сотрудники отдела {}: ", department);
                    for employee in employees {
                        println!("{}", employee);
                    }
                } else {
                    println!("Отдел {} не найден.", department);
                }
            }
            3 => {
                //все сотрудники компании
                println!("Все сотрудники компании:");
                let mut sorted_departments: Vec<_> = departments.keys().collect();
                sorted_departments.sort();//сортировка отделов по алфавиту

                for department in sorted_departments {
                    println!("Отдел {}:", department);
                    let employees = &departments[department];
                    for employee in employees {
                        println!("{}", employee);
                    }
                }
            }
            4 => {
                //выход
                println!("Выход...");
                break;
            }

            }
        }
    }
}