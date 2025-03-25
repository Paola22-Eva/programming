// структура, представляющая публикацию
struct Post {
    content: String,          // текстовое содержимое публикации
    state: Option<Box<dyn State>>, // состояние публикации (используем динамическую диспетчеризацию с помощью Box и трейта State)
}

// реализация методов для структуры Post
impl Post {
    // создаём новый экземпляр Post с пустым содержимым и состоянием Draft
    fn new() -> Post {
        Post {
            content: String::new(), // изначально контент пуст
            state: Some(Box::new(Draft {})), // публикация начинается в состоянии Draft
        }
    }

    // метод для добавления текста в публикацию
    fn add_text(&mut self, text: &str) {
        // проверяем, что текущее состояние публикации позволяет добавлять текст
        if self.state.as_ref().unwrap().is_draft() {
            self.content.push_str(text); // если состояние Draft, добавляем текст
        }
    }

    // метод для получения содержимого публикации
    fn content(&self) -> &str {
        // состояние определяет, что именно будет возвращено как содержимое
        self.state.as_ref().unwrap().content(self)
    }

    // метод для перехода публикации в состояние "На рассмотрении" (PendingReview)
    fn request_review(&mut self) {
        if let Some(s) = self.state.take() {
            // если состояние существует, заменяем его на состояние после запроса на рассмотрение
            self.state = Some(s.request_review());
        }
    }

    // метод для одобрения публикации
    fn approve(&mut self) {
        if let Some(s) = self.state.take() {
            // если состояние существует, заменяем его на состояние после одобрения
            self.state = Some(s.approve());
        }
    }

    // метод для отклонения публикации, возвращая состояние "Черновик"
    fn reject(&mut self) {
        if let Some(s) = self.state.take() {
            // если состояние существует, заменяем его на состояние "Черновик"
            self.state = Some(s.reject());
        }
    }
}

// трейт, описывающий возможные состояния
trait State {
    fn request_review(self: Box<Self>) -> Box<dyn State>; // запрос на рассмотрение
    fn approve(self: Box<Self>) -> Box<dyn State>;        // одобрение
    fn reject(self: Box<Self>) -> Box<dyn State> { self } // отклонение (по умолчанию возвращает сам объект)
    
    // метод для получения содержимого, который зависит от состояния
    fn content<'a>(&self, _post: &'a Post) -> &'a str {
        "" // возвращает пустую строку по умолчанию
    }

    // метод, определяющий, является ли состояние черновиком (Draft)
    fn is_draft(&self) -> bool {
        false
    }
}

// структура для состояния "Черновик"
struct Draft;

// реализация состояния "Черновик"
impl State for Draft {
    // при запросе на рассмотрение, переходим в состояние PendingReview
    fn request_review(self: Box<Self>) -> Box<dyn State> {
        Box::new(PendingReview {})
    }

    // состояние "Черновик" является черновиком
    fn is_draft(&self) -> bool {
        true
    }
}

// структура для состояния "На рассмотрении"
struct PendingReview;

// реализация состояния "На рассмотрении"
impl State for PendingReview {
    // при одобрении переходим в состояние PendingSecondReview
    fn approve(self: Box<Self>) -> Box<dyn State> {
        Box::new(PendingSecondReview {})
    }

    // при отклонении возвращаем состояние "Черновик"
    fn reject(self: Box<Self>) -> Box<dyn State> {
        Box::new(Draft {})
    }
}

// структура для состояния "На втором рассмотрении"
struct PendingSecondReview;

// реализация состояния "На втором рассмотрении"
impl State for PendingSecondReview {
    // при одобрении переходим в состояние "Опубликовано"
    fn approve(self: Box<Self>) -> Box<dyn State> {
        Box::new(Published {})
    }

    // при отклонении возвращаем состояние "Черновик"
    fn reject(self: Box<Self>) -> Box<dyn State> {
        Box::new(Draft {})
    }
}

// структура для состояния "Опубликовано"
struct Published;
// реализация состояния "Опубликовано"
impl State for Published {
    // в состоянии "Опубликовано" запрос на рассмотрение не имеет эффекта
    fn request_review(self: Box<Self>) -> Box<dyn State> {
        self
    }

    // в состоянии "Опубликовано" одобрение не имеет эффекта
    fn approve(self: Box<Self>) -> Box<dyn State> {
        self
    }

    // в состоянии "Опубликовано" возвращаем контент публикации
    fn content<'a>(&self, post: &'a Post) -> &'a str {
        &post.content // возвращаем настоящее содержимое
    }
}

// главная функция, где создаём и манипулируем публикацией
fn main() {
    let mut post = Post::new(); // создаём новый пост

    post.add_text("Первая версия текста."); // добавляем текст
    println!("Содержимое: {}", post.content()); // показываем содержимое (оно пустое)

    post.request_review(); // переходим в состояние "На рассмотрении"
    post.approve(); // одобряем публикацию
    println!("После первого approve: {}", post.content()); // содержимое всё ещё пустое

    post.approve(); // одобряем ещё раз, теперь публикация "Опубликована"
    println!("После второго approve: {}", post.content()); // показываем содержимое, которое теперь добавлено
}
