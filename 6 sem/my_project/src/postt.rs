pub struct Post {
    state: Option<Box<dyn State>>,
    content: String,
    approvals: u8, // Количество одобрений
}

impl Post {
    pub fn new() -> Post {
        Post {
            state: Some(Box::new(Draft {})),
            content: String::new(),
            approvals: 0,
        }
    }

    pub fn add_text(&mut self, text: &str) {
        if self.state.as_ref().unwrap().can_add_text() {
            self.content.push_str(text);
        }
    }

    pub fn content(&self) -> &str {
        self.state.as_ref().unwrap().content(self)
    }

    pub fn request_review(&mut self) {
        if let Some(s) = self.state.take() {
            self.state = Some(s.request_review());
        }
    }

    pub fn approve(&mut self) {
        if let Some(s) = self.state.take() {
            let (new_state, approvals) = s.approve(self.approvals);
            self.state = Some(new_state);
            self.approvals = approvals;
        }
    }

    pub fn reject(&mut self) {
        if let Some(s) = self.state.take() {
            self.state = Some(s.reject());
            self.approvals = 0; // Сбросить одобрения
        }
    }
}

trait State {
    fn request_review(self: Box<Self>) -> Box<dyn State>;
    fn approve(self: Box<Self>, approvals: u8) -> (Box<dyn State>, u8);
    fn reject(self: Box<Self>) -> Box<dyn State>;
    fn content<'a>(&self, _post: &'a Post) -> &'a str {
        ""
    }
    fn can_add_text(&self) -> bool {
        false
    }
}

struct Draft {}

impl State for Draft {
    fn request_review(self: Box<Self>) -> Box<dyn State> {
        Box::new(PendingReview {})
    }

    fn approve(self: Box<Self>, _approvals: u8) -> (Box<dyn State>, u8) {
        (self, 0) // Нельзя сразу одобрить
    }

    fn reject(self: Box<Self>) -> Box<dyn State> {
        self // Уже черновик, остаётся без изменений
    }

    fn can_add_text(&self) -> bool {
        true
    }
}

struct PendingReview {}

impl State for PendingReview {
    fn request_review(self: Box<Self>) -> Box<dyn State> {
        self // Уже на рассмотрении
    }

    fn approve(self: Box<Self>, approvals: u8) -> (Box<dyn State>, u8) {
        if approvals + 1 >= 2 {
            (Box::new(Published {}), 2)
        } else {
            (Box::new(PendingReview {}), approvals + 1)
        }
    }

    fn reject(self: Box<Self>) -> Box<dyn State> {
        Box::new(Draft {})
    }
}

struct Published {}

impl State for Published {
    fn request_review(self: Box<Self>) -> Box<dyn State> {
        self // Уже опубликовано
    }

    fn approve(self: Box<Self>, approvals: u8) -> (Box<dyn State>, u8) {
        (self, approvals) // Уже опубликовано
    }

    fn reject(self: Box<Self>) -> Box<dyn State> {
        self // Опубликованный пост нельзя отклонить
    }

    fn content<'a>(&self, post: &'a Post) -> &'a str {
        &post.content
    }
}