# RecordedFuture - Generic Detection (Very Malicious IPs and Domains)
author: Adrian Porcescu, Recorded Future

These playbook leverage the Recorded Future API to automate the import of the Recorded Future Risklists with [Very Malicious (Score 90+) IPs and Domains](https://support.recordedfuture.com/hc/en-us/articles/115000897208-Risk-Scoring-in-Recorded-Future), as tiIndicators, into the ThreatIntelligenceIndicator table, for detection (alerting) purposes in Azure Sentinel.  For additional information please visit [Recorded Future](https://www.recordedfuture.com/integrations/azure/).

Note: Due to internal Microsoft Logic Apps dependencies, please deploy first the ImportToSentinel playbook before the IndicatorProcessor one.

Links to deploy the RecordedFuture_Generic_Detection_ImportToSentinel playbook template:

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FAzure-Sentinel%2Fmaster%2FPlaybooks%2FRecordedFuture_Generic_Detection%2FRecordedFuture_Generic_Detection_ImportToSentinel.json" target="_blank">
	<img src="https://aka.ms/deploytoazurebutton"/>
</a>
<a href="https://portal.azure.us/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FAzure-Sentinel%2Fmaster%2FPlaybooks%2FRecordedFuture_Generic_Detection%2FRecordedFuture_Generic_Detection_ImportToSentinel.json" target="_blank">
	<img src="https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/1-CONTRIBUTION-GUIDE/images/deploytoazuregov.png"/>
</a>

Links to deploy the RecordedFuture_Generic_Detection_IndicatorProcessor playbook template:

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FAzure-Sentinel%2Fmaster%2FPlaybooks%2FRecordedFuture_Generic_Detection%2FRecordedFuture_Generic_Detection_IndicatorProcessor.json" target="_blank">
	<img src="https://aka.ms/deploytoazurebutton"/>
</a>
<a href="https://portal.azure.us/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FAzure-Sentinel%2Fmaster%2FPlaybooks%2FRecordedFuture_Generic_Detection%2FRecordedFuture_Generic_Detection_IndicatorProcessor.json" target="_blank">
	<img src="https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/1-CONTRIBUTION-GUIDE/images/deploytoazuregov.png"/>
</a>

