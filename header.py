def create_header():
    result = """
         <div class="header">
                <div class = "burger_plus_logo">
                    <button class="open-burger">
                        <img class = "carosel-body "src="./static/imgs/burg.webp" alt="">
                    </button>

                <form class="header-search" action="/">
                    <button class="header-search__button"><h1>AdSphere</h1></button>
                </form>
                </div>
                

                <div class="header-profile">
                    <form action="/sign">
                        <button id = "button-sign">Sign Up</button>
                    </form>
                    <form action="/login">
                        <button id = "button-log">Log In</button>
                    </form>
                    
                    
                   
                    <form class="profile-header-cont" action="/profile">
                        <button id = "button-profile"></button>
                        <span> Your Name</span>
                    </form>
                    
                   
                </div>
            </div>
    """
    return result