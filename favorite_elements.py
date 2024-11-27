def create_blogger_card():
    result = f"""

    <div class="blogger-card">
        <div class="blogger-card__info">
            <img class="blogger-card__img" src={"h"} alt="">
                <div class="blogger-card_name">
                    <span>{'Mirbek'}</span>
                    <a href="">{'@mirbek'}</a>
                </div>
            </div>
            <div class="blogger-card__buttons">
                <form action=""><button class="blogger-card__button_order">Order advertising</button></form>
                <form action=""><button class="blogger-card__button_delete">Delete</button></form>
            </div>
                                
        </div>
        <hr>

    """
    return result

def delete_blogger_card():
    pass