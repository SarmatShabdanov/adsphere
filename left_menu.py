
def create_left_menu():
    result = f"""
        <div class = "left-menu active">
            <button class="close-burger">CLOSE</button>
            <div class="button-contanier-head">
                <form action="/">
                    <button class="button-contanier">
                        <img class="img-cont" src="./static/imgs/compass-d.png" alt="">
                        <p>Home</p>
                    </button>
                </form>
                <form action="/favorite">
                    <button class="button-contanier">
                        <img class="img-cont" src=" ./static/imgs/fav.png" alt="">
                        <p class="button-cont">Favorite</p>
                    </button>
                </form>
                <form action="/search">
                    <button class="button-contanier">
                        <img class="img-cont" src="./static/imgs/search.png" alt="">
                        <p class="button-cont">Search</p>
                    </button>
                </form>
            </div>
            <form class="button-contanier-bottom" action="/profile">
                <button class="button-contanier">
                    <img class="img-cont" src="./static/imgs/profile.png" alt="">
                    <p class="button-cont">Profile</p>
                </button>
            </form>
        </div>

        
    """
    return result

def left_menu_create_script():
    result = """
        <script type="text/javascript">
            const burger = document.querySelector('.left-menu');
            const isOpen = Boolean(localStorage.getItem('isOpenBurger'));
            console.log(isOpen);
            
            if (isOpen){
                burger.classList.add('active')
            }else {
                burger.classList.remove('active')
            }
            document.querySelector('.close-burger').addEventListener('click', (e) => {
                burger.classList.remove('active')
                localStorage.removeItem('isOpenBurger')
            })
            document.querySelector('.open-burger').addEventListener('click', (e) => {
                burger.classList.add('active');
                localStorage.setItem('isOpenBurger', 'true')
            })
        </script>
    """
    return result