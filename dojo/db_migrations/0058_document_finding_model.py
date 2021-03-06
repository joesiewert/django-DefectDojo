# Generated by Django 2.2.16 on 2020-10-14 18:15

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import dojo.models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0057_ms_teams'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finding',
            name='active',
            field=models.BooleanField(default=True, help_text='Denotes if this flaw is active or not.', verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='component_name',
            field=models.CharField(blank=True, help_text='Name of the affected component (library name, part of a system, ...).', max_length=200, null=True, verbose_name='Component name'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='component_version',
            field=models.CharField(blank=True, help_text='Version of the affected component.', max_length=100, null=True, verbose_name='Component version'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='The date the finding was created inside DefectDojo.', null=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='cve',
            field=models.CharField(help_text='The Common Vulnerabilities and Exposures (CVE) associated with this flaw.', max_length=28, null=True, validators=[django.core.validators.RegexValidator(message="Vulnerability ID must be entered in the format: 'ABC-9999-9999'.", regex='^[A-Z]{1,10}(-\\d+)+$')], verbose_name='CVE'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='cvssv3',
            field=models.TextField(help_text='Common Vulnerability Scoring System version 3 (CVSSv3) score associated with this flaw.', max_length=117, null=True, validators=[django.core.validators.RegexValidator(message="CVSS must be entered in format: 'AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H'", regex='^AV:[NALP]|AC:[LH]|PR:[UNLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]')], verbose_name='CVSSv3'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='cwe',
            field=models.IntegerField(blank=True, default=0, help_text='The CWE number associated with this flaw.', null=True, verbose_name='CWE'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='date',
            field=models.DateField(default=dojo.models.get_current_date, help_text='The date the flaw was discovered.', verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='defect_review_requested_by',
            field=models.ForeignKey(blank=True, help_text='Documents who requested a defect review for this flaw.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='defect_review_requested_by', to='dojo.Dojo_User', verbose_name='Defect Review Requested By'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='description',
            field=models.TextField(help_text='Longer more descriptive information about the flaw.', verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='duplicate',
            field=models.BooleanField(default=False, help_text='Denotes if this flaw is a duplicate of other flaws reported.', verbose_name='Duplicate'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='duplicate_finding',
            field=models.ForeignKey(blank=True, editable=False, help_text='Link to the original finding if this finding is a duplicate.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='original_finding', to='dojo.Finding', verbose_name='Duplicate Finding'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='dynamic_finding',
            field=models.BooleanField(default=True, help_text='Flaw has been detected from a Dynamic Application Security Testing tool (DAST).', verbose_name='Dynamic finding (DAST)'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='endpoint_status',
            field=models.ManyToManyField(blank=True, help_text='The status of the endpoint associated with this flaw (Vulnerable, Mitigated, ...).', related_name='finding_endpoint_status', to='dojo.Endpoint_Status', verbose_name='Endpoint Status'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='endpoints',
            field=models.ManyToManyField(blank=True, help_text='The hosts within the product that are susceptible to this flaw.', to='dojo.Endpoint', verbose_name='Endpoints'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='false_p',
            field=models.BooleanField(default=False, help_text='Denotes if this flaw has been deemed a false positive by the tester.', verbose_name='False Positive'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='file_path',
            field=models.CharField(blank=True, help_text='Identified file(s) containing the flaw.', max_length=4000, null=True, verbose_name='File path'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='found_by',
            field=models.ManyToManyField(editable=False, help_text='The name of the scanner that identified the flaw.', to='dojo.Test_Type', verbose_name='Found by'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='hash_code',
            field=models.CharField(blank=True, editable=False, help_text='A hash over a configurable set of fields that is used for findings deduplication.', max_length=64, null=True, verbose_name='Hash Code'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='images',
            field=models.ManyToManyField(blank=True, help_text='Image(s) / Screenshot(s) related to the flaw.', to='dojo.FindingImage', verbose_name='Images'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='impact',
            field=models.TextField(help_text='Text describing the impact this flaw has on systems, products, enterprise, etc.', verbose_name='Impact'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='is_Mitigated',
            field=models.BooleanField(default=False, help_text='Denotes if this flaw has been fixed.', verbose_name='Is Mitigated'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='is_template',
            field=models.BooleanField(default=False, help_text='Denotes if this finding is a template and can be reused.', verbose_name='Is Template'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='jira_change',
            field=models.DateTimeField(help_text='The date the linked Jira issue was last modified.', null=True, verbose_name='Jira change'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='jira_creation',
            field=models.DateTimeField(help_text='The date a Jira issue was created from this finding.', null=True, verbose_name='Jira creation'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='last_reviewed',
            field=models.DateTimeField(editable=False, help_text="Provides the date the flaw was last 'touched' by a tester.", null=True, verbose_name='Last Reviewed'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='last_reviewed_by',
            field=models.ForeignKey(editable=False, help_text='Provides the person who last reviewed the flaw.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='last_reviewed_by', to=settings.AUTH_USER_MODEL, verbose_name='Last Reviewed By'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='line',
            field=models.IntegerField(blank=True, help_text='Source line number of the attack vector.', null=True, verbose_name='Line number'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='line_number',
            field=models.CharField(blank=True, editable=False, help_text='Deprecated will be removed, use line', max_length=200, null=True, verbose_name='Line Number'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='mitigated',
            field=models.DateTimeField(blank=True, editable=False, help_text='Denotes if this flaw has been fixed by storing the date it was fixed.', null=True, verbose_name='Mitigated'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='mitigated_by',
            field=models.ForeignKey(editable=False, help_text='Documents who has marked this flaw as fixed.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mitigated_by', to=settings.AUTH_USER_MODEL, verbose_name='Mitigated By'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='mitigation',
            field=models.TextField(help_text='Text describing how to best fix the flaw.', verbose_name='Mitigation'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='nb_occurences',
            field=models.IntegerField(blank=True, help_text='Number of occurences in the source tool when several vulnerabilites were found and aggregated by the scanner.', null=True, verbose_name='Number of occurences'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='notes',
            field=models.ManyToManyField(blank=True, editable=False, help_text='Stores information pertinent to the flaw or the mitigation.', to='dojo.Notes', verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='numerical_severity',
            field=models.CharField(help_text='The numerical representation of the severity (S0, S1, S2, S3, S4).', max_length=4, verbose_name='Numerical Severity'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='out_of_scope',
            field=models.BooleanField(default=False, help_text='Denotes if this flaw falls outside the scope of the test and/or engagement.', verbose_name='Out Of Scope'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='param',
            field=models.TextField(blank=True, editable=False, help_text='Parameter used to trigger the issue (DAST).', null=True, verbose_name='Parameter'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='payload',
            field=models.TextField(blank=True, editable=False, help_text='Payload used to attack the service / application and trigger the bug / problem.', null=True, verbose_name='Payload'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='references',
            field=models.TextField(blank=True, db_column='refs', help_text='The external documentation available for this flaw.', null=True, verbose_name='References'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='reporter',
            field=models.ForeignKey(default=1, editable=False, help_text='Documents who reported the flaw.', on_delete=django.db.models.deletion.CASCADE, related_name='reporter', to=settings.AUTH_USER_MODEL, verbose_name='Reporter'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='review_requested_by',
            field=models.ForeignKey(blank=True, help_text='Documents who requested a review for this finding.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review_requested_by', to='dojo.Dojo_User', verbose_name='Review Requested By'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='reviewers',
            field=models.ManyToManyField(blank=True, help_text='Documents who reviewed the flaw.', to=settings.AUTH_USER_MODEL, verbose_name='Reviewers'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='sast_sink_object',
            field=models.CharField(blank=True, help_text='Sink object (variable, function...) of the attack vector.', max_length=500, null=True, verbose_name='SAST Sink Object'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='sast_source_file_path',
            field=models.CharField(blank=True, help_text='Source file path of the attack vector.', max_length=4000, null=True, verbose_name='SAST Source File Path'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='sast_source_line',
            field=models.IntegerField(blank=True, help_text='Source line number of the attack vector.', null=True, verbose_name='SAST Source Line number'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='sast_source_object',
            field=models.CharField(blank=True, help_text='Source object (variable, function...) of the attack vector.', max_length=500, null=True, verbose_name='SAST Source Object'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='scanner_confidence',
            field=models.IntegerField(blank=True, default=None, editable=False, help_text='Confidence level of vulnerability which is supplied by the scanner.', null=True, verbose_name='Scanner confidence'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='severity',
            field=models.CharField(help_text='The severity level of this flaw (Critical, High, Medium, Low, Informational).', max_length=200, verbose_name='Severity'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='severity_justification',
            field=models.TextField(blank=True, help_text='Text describing why a certain severity was associated with this flaw.', null=True, verbose_name='Severity Justification'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='sonarqube_issue',
            field=models.ForeignKey(blank=True, help_text='The SonarQube issue associated with this finding.', null=True, on_delete=django.db.models.deletion.CASCADE, to='dojo.Sonarqube_Issue', verbose_name='SonarQube issue'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='sourcefile',
            field=models.TextField(blank=True, editable=False, help_text='Name of the source code file in which the flaw is located.', null=True, verbose_name='Source File'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='sourcefilepath',
            field=models.TextField(blank=True, editable=False, help_text='Filepath of the source code file in which the flaw is located.', null=True, verbose_name='Source File Path'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='static_finding',
            field=models.BooleanField(default=False, help_text='Flaw has been detected from a Static Application Security Testing tool (SAST).', verbose_name='Static finding (SAST)'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='steps_to_reproduce',
            field=models.TextField(blank=True, help_text='Text describing the steps that must be followed in order to reproduce the flaw / bug.', null=True, verbose_name='Steps to Reproduce'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='test',
            field=models.ForeignKey(editable=False, help_text='The test that is associated with this flaw.', on_delete=django.db.models.deletion.CASCADE, to='dojo.Test', verbose_name='Test'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='thread_id',
            field=models.IntegerField(default=0, editable=False, verbose_name='Thread ID'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='title',
            field=models.CharField(help_text='A short description of the flaw.', max_length=511, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='under_defect_review',
            field=models.BooleanField(default=False, help_text='Denotes if this finding is under defect review.', verbose_name='Under Defect Review'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='under_review',
            field=models.BooleanField(default=False, help_text='Denotes is this flaw is currently being reviewed.', verbose_name='Under Review'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='unique_id_from_tool',
            field=models.CharField(blank=True, help_text='Vulnerability technical id from the source tool. Allows to track unique vulnerabilities.', max_length=500, null=True, verbose_name='Unique ID from tool'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='url',
            field=models.TextField(blank=True, editable=False, help_text='External reference that provides more information about this flaw.', null=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='verified',
            field=models.BooleanField(default=True, help_text='Denotes if this flaw has been manually verified by the tester.', verbose_name='Verified'),
        ),
    ]
