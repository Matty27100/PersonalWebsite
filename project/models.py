from django.db import models
from storages.backends.gcloud import GoogleCloudStorage
gcs_storage = GoogleCloudStorage()

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.TextField(help_text="List technologies used, separated by commas")  # Changed from CharField to TextField
    image = models.ImageField(storage=gcs_storage, upload_to='pictures/')
    url = models.URLField(blank=True)  # Make URL optional
    github_url = models.URLField(blank=True, help_text="Link to GitHub repository")
    status = models.CharField(
        max_length=20, 
        choices=[('completed', 'Completed'), ('in_progress', 'In Progress'), ('planned', 'Planned')],
        default='in_progress'
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Activity(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_range = models.CharField(max_length=50)  # e.g., "April 2024 - Present"
    image = models.ImageField(storage=gcs_storage, upload_to='activities/')
    highlight_words = models.CharField(
        max_length=255, 
        blank=True,
        help_text="Comma-separated list of words to highlight in the description"
    )
    order = models.IntegerField(default=0, help_text="Order in which this activity appears (lower numbers appear first)")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Activities"
        ordering = ['order', '-created_at']  # Order by the order field first, then by created_at