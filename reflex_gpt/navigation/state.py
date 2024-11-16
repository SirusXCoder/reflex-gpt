import reflex as  rx

from  . import routes

class NavState(rx.State):
    def to_home(self):
        """
            ON CLICK EVENT
        """
        print("clicked home")
        return rx.redirect(routes.HOME_ROUTE)
    
    def to_about_us(self):
        """
            ON CLICK EVENT
        """
        print("clicked about")
        return rx.redirect(routes.ABOUT_US_ROUTE)
    
