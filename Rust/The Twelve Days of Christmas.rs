fn main() {
    // Список подарков для каждого дня
    let gifts_for_every_day = [
        "A partridge in a pear tree",
        "Two turtle doves",
        "Three french hens",
        "Four calling birds",
        "Five gold rings",
        "Six geese a-laying",
        "Seven swans a-swimming",
        "Eight maids a-milking",
        "Nine ladies dancing",
        "Ten lords a-leaping",
        "Eleven pipers piping",
        "Twelve drummers drumming"
    ];

    ////цикл каждого из 12 дней
    for day in (1..12) {
        //первая строчка песни каждого дня
        println!("On the {} day of Christmas my true love gave to me:", day);
        
        if day < 2 {
            println!("A partridge in a pear tree");
            }
        else {
        //вывод всех подарков в обратном порядке
            for gift in gifts_for_every_day[..day].iter().rev() {
            //добавление "and" перед первым подарком
                if gift == &"A partridge in a pear tree"{
                    print!("and ");}
                println!("{}", gift);
            }
        }
        //вывод для удобства пустой строки между днями
        println!();
    }
}
