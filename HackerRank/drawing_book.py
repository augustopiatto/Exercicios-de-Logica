def page_count(pages_length, goal_page):
    import math

    end_to_goal_distance = (
        pages_length + 1 - goal_page) if pages_length % 2 == 0 else (pages_length - goal_page)
    start_to_goal_distance = goal_page

    return math.floor(end_to_goal_distance / 2) if end_to_goal_distance < start_to_goal_distance else math.floor(start_to_goal_distance / 2)


def test_page_count():
    book_pages_length = 6
    desired_page = 5

    result = page_count(book_pages_length, desired_page)

    assert result == 1
