<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:output method="text" encoding="UTF-8"/>
<!--
SAMPLE DATA:
<applicationbuilds xmlns:xsi="http&#x3a;&#x2f;&#x2f;www.w3.org&#x2f;2001&#x2f;XMLSchema-instance" xmlns="https&#x3a;&#x2f;&#x2f;analysiscenter.veracode.com&#x2f;schema&#x2f;2.0&#x2f;applicationbuilds" xsi:schemaLocation="https&#x3a;&#x2f;&#x2f;analysiscenter.veracode.com&#x2f;schema&#x2f;2.0&#x2f;applicationbuilds https&#x3a;&#x2f;&#x2f;analysiscenter.veracode.com&#x2f;resource&#x2f;2.0&#x2f;applicationbuilds.xsd" account_id="34738">

  <application app_name="NPEP Outbound C5" app_id="451137" industry_vertical="Communications" assurance_level="High" business_criticality="High" origin="Internally Developed" modified_date="2019-01-28T15&#x3a;25&#x3a;02-05&#x3a;00" cots="false" business_unit="Enterprise" business_owner="Doug Burco" tags="Outbound">
      <customfield name="Product" value=""/>
      <customfield name="Line of Business" value="Outbound"/>
      <customfield name="Version" value=""/>
      <customfield name="Components" value=""/>
      <customfield name="Documentation URL" value=""/>
      <customfield name="Code Repo URL" value=""/>
      <customfield name="Artifacts Repo URL" value=""/>
      <customfield name="Code Review Tool URL" value=""/>
      <customfield name="Custom 9" value=""/>
      <customfield name="Custom 10" value=""/>

      <build version="23 Jan 2019 Dynamic" build_id="3453093" submitter="Gordon Duke" platform="Not Specified" lifecycle_stage="Not Specified" results_ready="true" policy_name="Nuance PCI " policy_version="6" policy_compliance_status="Did Not Pass" rules_status="Did Not Pass" grace_period_expired="true" scan_overdue="false">
         <analysis_unit analysis_type="Dynamic" published_date="2019-01-28T15&#x3a;24&#x3a;49-05&#x3a;00" published_date_sec="1548707089" status="Results Ready"/>
      </build>

  </application>
-->

    <xsl:template match="/">
        <xsl:text>AppName,AppId,BU,Owner,Product,LOB,DocUrl,CodeRepoUrl,ArtifactsRepoUrl,CodeReviewToolUrl,LastBuildVersion,LastBuildId,LastSubmitter,PolicyName,PolicyComplianceStatus,GracePeriodExpired</xsl:text>
        <xsl:text>&#xA;</xsl:text>
        <xsl:for-each select="*/*">

            <!-- application attributes -->
            <xsl:value-of select="concat('&quot;', translate(@app_name, ',', ';'), '&quot;')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="concat('&quot;', @app_id, '&quot;')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="concat('&quot;', translate(@business_unit, ',', ';'), '&quot;')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="concat('&quot;', translate(@business_owner, ',', ';'), '&quot;')"/>
            <xsl:text>,</xsl:text>

            <!-- customfield attributes -->
            <xsl:value-of select="concat('&quot;', translate(*[@name='Product']/@value, ',', ';'), '&quot;')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="concat('&quot;', translate(*[@name='Line of Business']/@value, ',', ';'), '&quot;')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="concat('&quot;', translate(*[@name='Documentation URL']/@value, ',', ';'), '&quot;')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="concat('&quot;', translate(*[@name='Code Repo URL']/@value, ',', ';'), '&quot;')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="concat('&quot;', translate(*[@name='Artifacts Repo URL']/@value, ',', ';'), '&quot;')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="concat('&quot;', translate(*[@name='Code Review Tool URL']/@value, ',', ';'), '&quot;')"/>
            <xsl:text>,</xsl:text>

            <!-- build attributes -->
            <xsl:value-of select="concat('&quot;', translate(*/@version, ',', ';'), '&quot;')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="concat('&quot;', */@build_id, '&quot;')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="concat('&quot;', translate(*/@submitter, ',', ';'), '&quot;')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="concat('&quot;', translate(*/@policy_name, ',', ';'), '&quot;')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="concat('&quot;', translate(*/@policy_compliance_status, ',', ';'), '&quot;')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="concat('&quot;', translate(*/@grace_period_expired, ',', ';'), '&quot;')"/>
            <xsl:text>&#xA;</xsl:text>

        </xsl:for-each>
    </xsl:template>

</xsl:stylesheet>

