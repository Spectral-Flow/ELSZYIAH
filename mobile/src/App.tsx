/**
 * Elysia Concierge Mobile App
 * The Avant - Centennial, Colorado
 * 
 * Main application entry point
 */

import React from 'react';
import {
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  View,
  TouchableOpacity,
  Alert,
} from 'react-native';

const App = () => {
  const handleFeaturePress = (feature: string) => {
    Alert.alert(
      `${feature} Feature`,
      `${feature} functionality will be available in the full app release.`,
      [{ text: 'OK' }]
    );
  };

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar backgroundColor="#667eea" barStyle="light-content" />
      
      <View style={styles.header}>
        <Text style={styles.logo}>🏢</Text>
        <Text style={styles.title}>Elysia Concierge</Text>
        <Text style={styles.subtitle}>The Avant - Centennial, CO</Text>
      </View>

      <ScrollView style={styles.content}>
        <View style={styles.status}>
          <Text style={styles.statusText}>✅ System Online</Text>
          <Text style={styles.statusSubtext}>AI Concierge ready to assist 24/7</Text>
        </View>

        <View style={styles.features}>
          <TouchableOpacity 
            style={styles.featureCard}
            onPress={() => handleFeaturePress('Maintenance')}
          >
            <Text style={styles.featureIcon}>🔧</Text>
            <Text style={styles.featureTitle}>Maintenance</Text>
            <Text style={styles.featureDesc}>Request repairs & service</Text>
          </TouchableOpacity>

          <TouchableOpacity 
            style={styles.featureCard}
            onPress={() => handleFeaturePress('Amenities')}
          >
            <Text style={styles.featureIcon}>🏋️</Text>
            <Text style={styles.featureTitle}>Amenities</Text>
            <Text style={styles.featureDesc}>Book fitness & facilities</Text>
          </TouchableOpacity>

          <TouchableOpacity 
            style={styles.featureCard}
            onPress={() => handleFeaturePress('Community')}
          >
            <Text style={styles.featureIcon}>🏘️</Text>
            <Text style={styles.featureTitle}>Community</Text>
            <Text style={styles.featureDesc}>Events & updates</Text>
          </TouchableOpacity>

          <TouchableOpacity 
            style={styles.featureCard}
            onPress={() => handleFeaturePress('Packages')}
          >
            <Text style={styles.featureIcon}>📦</Text>
            <Text style={styles.featureTitle}>Packages</Text>
            <Text style={styles.featureDesc}>Delivery tracking</Text>
          </TouchableOpacity>
        </View>

        <View style={styles.footer}>
          <Text style={styles.footerTitle}>Kairoi Residential Technology</Text>
          <Text style={styles.footerSubtitle}>Making apartment living extraordinary</Text>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f7fafc',
  },
  header: {
    backgroundColor: '#667eea',
    padding: 24,
    alignItems: 'center',
  },
  logo: {
    fontSize: 48,
    marginBottom: 8,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: 'white',
    marginBottom: 4,
  },
  subtitle: {
    fontSize: 16,
    color: 'rgba(255,255,255,0.8)',
  },
  content: {
    flex: 1,
    padding: 16,
  },
  status: {
    backgroundColor: '#f0fff4',
    borderColor: '#68d391',
    borderWidth: 1,
    borderRadius: 8,
    padding: 16,
    marginBottom: 24,
    alignItems: 'center',
  },
  statusText: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#2f855a',
    marginBottom: 4,
  },
  statusSubtext: {
    fontSize: 14,
    color: '#2f855a',
  },
  features: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
    marginBottom: 24,
  },
  featureCard: {
    backgroundColor: 'white',
    borderRadius: 12,
    padding: 16,
    width: '48%',
    marginBottom: 16,
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  featureIcon: {
    fontSize: 32,
    marginBottom: 8,
  },
  featureTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#2d3748',
    marginBottom: 4,
  },
  featureDesc: {
    fontSize: 12,
    color: '#718096',
    textAlign: 'center',
  },
  footer: {
    alignItems: 'center',
    paddingTop: 16,
    borderTopColor: '#e2e8f0',
    borderTopWidth: 1,
  },
  footerTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#2d3748',
    marginBottom: 4,
  },
  footerSubtitle: {
    fontSize: 14,
    color: '#718096',
  },
});

export default App;