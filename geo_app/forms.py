from django import forms



# ip address form 
class AddressForm(forms.Form):
    ip_address = forms.CharField(max_length=18, required=True)

    # clean ip_form 
    def clean_ip_address(self):
        ip_address = self.cleaned_data["ip_address"]

        # if not all(i.isdigit() for i in ip_address ):
        #     return forms.ValidationError("Ip address must be a number")
        if ip_address == " ":
            return forms.ValidationError("Ip cannot be empty")
        
        return ip_address
