// главная функция, где создаём и манипулируем публикацией
mod postt;
use post::Post;
fn main() {
    let mut post = Post::new();

    post.add_text("Hello, Rust!");
    assert_eq!("", post.content()); // В черновике контент недоступен

    post.request_review();
    assert_eq!("", post.content()); // Пока на рассмотрении, контент тоже недоступен

    post.approve();
    assert_eq!("", post.content()); // Нужно второе одобрение

    post.approve();
    assert_eq!("Hello, Rust!", post.content()); // Теперь опубликовано!

    post.reject(); // После публикации отклонение не работает
    assert_eq!("Hello, Rust!", post.content()); // Всё ещё опубликовано

    let mut post2 = Post::new();
    post2.add_text("Another Post");
    post2.request_review();
    post2.reject(); // Отклоняем обратно в Draft
    post2.add_text(" - More Content");
    post2.request_review();
    post2.approve();
    post2.approve();
    assert_eq!("Another Post - More Content", post2.content());
}