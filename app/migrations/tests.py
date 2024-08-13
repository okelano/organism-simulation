from django.test import TestCase

# Example test
class ExampleModelTest(TestCase):
    def test_string_representation(self):
        example = ExampleModel(name="Example")
        self.assertEqual(str(example), example.name)
