# (write from-class)
from django import forms


class StudentForm(forms.Form):
    name = forms.CharField()
    marks = forms.IntegerField()


class StudentLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


def starts_with_s(value):
    if value[0].lower() != 's':
        raise forms.ValidationError('Name should starts with s or S only...')


# (already-done, re-use-it)
from django import forms


class FeedBackForm(forms.Form):
    # name = forms.CharField()
    # name = forms.CharField(validators=[starts_with_s])
    # rollno = forms.IntegerField()
    # email = forms.EmailField()
    # feedback = forms.CharField(widget=forms.Textarea)
    # feedback = forms.CharField(widget=forms.Textarea, validators=[validators.MinLengthValidator(10), validators.MaxLengthValidator(30)])
    name = forms.CharField()
    rollno = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)

    def clean(self):
        print('Total Form validation... is getting done!!!')

        total_cleaned_data = super().clean()  # gets complete form submitted data
        inputname = total_cleaned_data['name']
        if inputname[0].lower() != 's':
            raise forms.ValidationError('Name parameter should start with S or s only...');
        inputrollno = total_cleaned_data['rollno']
        if inputrollno <= 0:
            raise forms.ValidationError('Rollno should be > 0...')
        inputfeedback = total_cleaned_data['feedback']
        if len(inputfeedback) < 10 or len(inputfeedback) > 50:
            raise forms.ValidationError('Feedback should be min 10-chars & max 50-chars...')

    # other core validators using django
    # name = forms.CharField(validators=[validators.RegexValidator('[ASGZ].*')])
    # rollno = forms.IntegerField(validators=[validators.RegexValidator('[6-9]\d{5}')])
    # email = forms.EmailField(validators=[validators.EmailValidator])


'''
	def clean_name(self):
		print('validating name-field...');
		inputname = self.cleaned_data['name'];
		if len(inputname) < 5:
			raise forms.ValidationError('Min. no-of-chars in name-field should be 5..!!');
		return inputname;

	def clean_rollno(self):
		inputrollno = self.cleaned_data['rollno'];
		print('Validating rollno-field...');
		if inputrollno == 0:
			raise forms.ValidationError('Roll-number field cannot be EMPTY or ZERO...');
		return inputrollno;

	def clean_email(self):
		inputemail = self.cleaned_data['email'];
		print("Validating email-field...");
		if len(inputemail) < 8:
			raise forms.ValidationError('Email-field cannot be EMPTY or less than 3-chars...');
		return inputemail;

	def clean_feedback(self):
		inputfeedback = self.cleaned_data['feedback']
		print("Validating feedback-field...");
		if len(inputfeedback) < 3:
			raise forms.ValidationError('Feedback-field cannot be less than 3-chars...');
		return inputfeedback
		'''
