<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:output method="text" encoding="UTF-8"/>

    <xsl:template match="/">
        <xsl:text>AppName,AppId,BU,Owner,LOB</xsl:text>
        <xsl:text>&#xA;</xsl:text>
        <xsl:for-each select="*/*/*">
          <xsl:if test="@name='Line of Business'">
            <xsl:value-of select="concat('&quot;', ../@app_name, '&quot;')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="concat('&quot;', ../@app_id, '&quot;')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="concat('&quot;', ../@business_unit, '&quot;')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="concat('&quot;', ../@business_owner, '&quot;')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="concat('&quot;', @value, '&quot;')"/>
            <xsl:text>&#xA;</xsl:text>
          </xsl:if>
        </xsl:for-each>
    </xsl:template>

</xsl:stylesheet>

