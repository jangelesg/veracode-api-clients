<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:output method="text" encoding="UTF-8"/>

    <xsl:template match="/">
        <xsl:text>AppName,AppId,Version,BuildId,Submitter,PolicyName,PolicyComplianceStatus,GracePeriodExpired</xsl:text>
        <xsl:text>&#xA;</xsl:text>
        <xsl:for-each select="*/*/*">
          <xsl:if test="@version">
            <xsl:value-of select="concat('&quot;', ../@app_name, '&quot;')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="concat('&quot;', ../@app_id, '&quot;')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="concat('&quot;', @version, '&quot;')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="concat('&quot;', @build_id, '&quot;')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="concat('&quot;', @submitter, '&quot;')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="concat('&quot;', @policy_name, '&quot;')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="concat('&quot;', @policy_compliance_status, '&quot;')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="concat('&quot;', @grace_period_expired, '&quot;')"/>
            <xsl:text>&#xA;</xsl:text>
          </xsl:if>
        </xsl:for-each>
    </xsl:template>

</xsl:stylesheet>

